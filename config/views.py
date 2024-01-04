from django.shortcuts import render

def terms_of_service(request):
    # 'terms_of_service.html' はあなたの利用規約テンプレートのファイル名です
    return render(request, 'collect/terms_of_service.html')
def policy(request):
    return render(request, 'collect/policy.html')
