from website import create_app

app = create_app()
#if only if we run the main.py file then only app should run, not when we import the main.py file.
if __name__ == '__main__':
    #run the application. start the web server. debug=True beacuse we want to re run the web server for every change in the .py file.
    app.run(debug=True)