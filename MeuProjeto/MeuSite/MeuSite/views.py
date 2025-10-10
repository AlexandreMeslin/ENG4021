from django.shortcuts import render

def home(request):
    '''
    View function for home page of site.
    Renders the home.html template.
    This will display the home page when the root URL is accessed
    The home view is responsible for displaying the content of the home page
    It is a simple function-based view
    It takes a request object as a parameter
    It returns a rendered HTML response
    @param request: The HTTP request object
    @return: Rendered HTML response with home page content
    '''
    return render(request, 'MeuSite/home.html')