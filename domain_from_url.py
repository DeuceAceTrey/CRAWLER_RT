def get_domain_from_url(url):
    
    from urllib.parse import urlparse
    parsed_url = urlparse(url)
    try:
        filename = parsed_url.netloc
    except:
        # Si falla es porque la implementación de parsed_url no reconoce los atributos como "path"
        if len(parsed_url)>=4:
            filename = parsed_url[1]
        else:
            filename = ""

    return filename

print(get_domain_from_url('https://www.ripoffreport.com/reports/specific_search/australia'))