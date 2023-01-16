import win10toast

if __name__ == '__main__':
    toaster = win10toast.ToastNotifier()
    toaster.show_toast("Заголовок", "Описание уведомления")