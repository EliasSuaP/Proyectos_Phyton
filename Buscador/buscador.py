import requests
from bs4 import BeautifulSoup

url = "https://www.laborum.cl/en-region-metropolitana/empleos-publicacion-hoy-busqueda-psicologo.html"

if "__main__" == __name__:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    def has_data_search(tag):
        return tag.has_attr("sc-gyFTku NNeLf")

    results = soup.find_all(has_data_search)

    for job in results:
        try:
            titleElement = job.find("div", attrs={"class": "sc-dcmekm"})
            title = titleElement.get_text()
            company = job.find("div", attrs={"class": "sc-jklikk"}).get_text()
            joblink = "https://www.laborum.cl" + titleElement["href"]
            #salary = job.find("span", attrs={"data-automation": "jobSalary"})
            #salary = salary.get_text() if salary else 'n/a'

            job = "Titulo: {}\nEmpresa: {}\nLink: {}a\n"

            job = job.format(title, company, joblink)
            
            print(job)
        except Exception as e:
            print("Exception: {}".format(e))
            pass