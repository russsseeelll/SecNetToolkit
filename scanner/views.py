from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import ScanForm
import subprocess
import shlex

def index(request):
    """
    Renders the main page and handles the form rendering for GET requests.
    """
    if request.method == "GET":
        form = ScanForm()
        return render(request, "scanner/index.html", {"form": form})
    elif request.method == "POST":
        form = ScanForm()
        return render(request, "scanner/index.html", {"form": form})

@csrf_exempt
def run_scan(request):
    if request.method == "POST":
        target = request.POST.get("target", "").strip()
        action = request.POST.get("action", "").strip()

        if not target or not action:
            return JsonResponse({"error": "Both target and action are required."}, status=400)

        target_sanitized = shlex.quote(target)
        commands = {
            "nmap_common": f"nmap -Pn --top-ports 1000 {target_sanitized}",
            "nmap_full": f"nmap -Pn -p- {target_sanitized}",
            "nslookup": f"nslookup {target_sanitized}",
            "whois": f"whois {target_sanitized}",
            "dig": f"dig {target_sanitized}",
            "traceroute": f"traceroute -q 1 {target_sanitized}",
            "sslscan": f"sslscan --timeout=10 {target_sanitized}",
        }

        cmd = commands.get(action)
        if not cmd:
            return JsonResponse({"error": "Invalid action selected."}, status=400)

        try:
            result = subprocess.run(
                shlex.split(cmd),
                capture_output=True,
                text=True,
                timeout=120,  # Increase timeout to allow longer scans
            )
            return JsonResponse({"output": result.stdout + result.stderr}, status=200)
        except subprocess.TimeoutExpired:
            return JsonResponse({"error": f"The command '{action}' timed out."}, status=500)
        except Exception as e:
            return JsonResponse({"error": f"Unexpected error: {str(e)}"}, status=500)

    return JsonResponse({"error": "Invalid request method."}, status=405)
