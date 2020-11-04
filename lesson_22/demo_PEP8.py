def return_first_arg(*args, **kwargs):
    """
    Foo return the first argument i foo call.
    :param args:
    :return:
    """
    print("+" * 40)
    print("Call Foo")
    print(args, kwargs)
    return None or args[0]


print(return_first_arg("Hello", 12))
rez = return_first_arg("hello", "World", 2020, name="Taras", pape_to_visite="www.google.com",
                       signature="mail@google.com", text_var="sdfsdfsfsdfsd")
print(rez)
del rez
