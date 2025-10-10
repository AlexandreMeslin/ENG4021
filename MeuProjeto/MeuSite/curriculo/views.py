from django.shortcuts import render

# Create your views here.

def curriculo_spiff(request):
    '''
    View function for the astronaut Spiff's resume page.
    Renders the curriculo-v1.html template.
    This will display the resume page when the corresponding URL is accessed
    The curriculo_spiff view is responsible for displaying the content of the resume page
    It is a simple function-based view
    It takes a request object as a parameter
    It returns a rendered HTML response
    @param request: The HTTP request object
    @return: Rendered HTML response with resume page content
    '''
    return render(request, 'curriculo/curriculo-v1.html')

def curriculo_spiff_v2(request):
    '''
    View function for the astronaut Spiff's resume page version 2.
    A responsive version of the resume page.
    Renders the curriculo-v2.html template.
    This will display the resume page version 2 when the corresponding URL is accessed
    The curriculo_spiff_v2 view is responsible for displaying the content of the resume page version 2
    It is a simple function-based view
    It takes a request object as a parameter
    It returns a rendered HTML response
    @param request: The HTTP request object
    @return: Rendered HTML response with resume page version 2 content
    '''
    return render(request, 'curriculo/curriculo-v2.html')