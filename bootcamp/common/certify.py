def check_form(request):
    has_data = 0
    for data in request.POST.items():
        for d in data:
            if d == "certificate_number":
                has_data += 1

    if has_data != 1:
        return False
    
    return True


def check_fields(request):
    if not request.POST['certificate_number']:
        return False
    return True