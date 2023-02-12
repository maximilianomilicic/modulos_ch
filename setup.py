from setuptools import setup

setup(

    name= "Mi primer paquete",
    version= "1.0",
    description= "estamos haciendo el primer paquete redistribuible",
    author= "maximiliano milicic",
    author_email= "maximiliano.milicic@gmail.com",

    packages=["mi_paquete"]
   


)

# para hacer el paquete distribuible hay que poner en la terminal esoto  ----->   python setup.py sdist