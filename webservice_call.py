#!/usr/bin/python
 
from SOAPpy import WSDL
 
#The location of our webservice description
WSDLFile = "http://www.webservicex.net/country.asmx?WSDL"
 
#Object to handle the requests and responses from our
#webservice
proxy = WSDL.Proxy(WSDLFile)
 
#This will print the documentation of the Proxy class
print proxy.__doc__
#This will print all the available methods and parameters
#in the webservice
print proxy.methods.keys()
 
#Some of the properties of the SOAP object.
print(proxy.soapproxy.namespace)
print(proxy.soapproxy.soapaction)
print(proxy.wsdl)
 
#You can use this to access each method
#of the webservice.
#for method in proxy.methods.keys() :
# ci = proxy.methods[method]
# for param in ci.outparams :
# print param.name.ljust(20) , param.type
 
currencies = proxy.GetCurrencies()
 
#This will print the XML returned by the webservice
print(currencies)
