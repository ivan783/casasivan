
def global_variables(request):
    """
      The context processor must return a dictionary.
    """
    return {
        'domain_name': 'Super-Casas',
        'domain': "https://super-casa.tornode.org",
    }
