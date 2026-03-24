%define module lxml-html-clean
%define oname lxml_html_clean

Name:		python-lxml-html-clean
Version:	0.4.4
Release:	1
Summary:	HTML cleaner from lxml project
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://pypi.org/project/lxml-html-clean/
Source0:	https://files.pythonhosted.org/packages/source/l/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
HTML cleaner from lxml project

%files
%doc README.md
%license LICENSE.txt
%{py_sitedir}/%{oname}
%{py_sitedir}/%{oname}-%{version}.dist-info
