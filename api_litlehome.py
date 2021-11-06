def litleHomeApi_main(request, command):
    request.send_response(200)
    request.end_headers()
    print("     -> Запрошена команда: ", end="")
    print(command)
    print("   ->| Запрос к макету обработан")