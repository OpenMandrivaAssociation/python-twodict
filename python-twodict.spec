%define module	twodict

Name:		python-%{module}
Version:	1.2
Release:	1
Summary:	Simple two-way ordered dictionary for Python
License:	Public Domain
Group:		Development/Python
Url:		https://github.com/MrS0m30n3/twodict
Source0:	https://files.pythonhosted.org/packages/source/t/twodict/%{module}-%{version}.tar.gz
BuildArch:      noarch

%description
TwoWayOrderedDict is a custom dictionary in which one can get the
key:value relationship but can also get the value:key relationship.
It also remembers the order in which the items were inserted and
supports almost all the features of the built-in dict.

%package -n	python2-%{module}
Summary:	Simple two-way ordered dictionary for Python 2
Group:		Development/Python
BuildArch:      noarch
BuildRequires:	pkgconfig(python2)
BuildRequires:	pythonegg(setuptools)

%description -n	python2-%{module}
TwoWayOrderedDict is a custom dictionary in which one can get the
key:value relationship but can also get the value:key relationship.
It also remembers the order in which the items were inserted and
supports almost all the features of the built-in dict.

#------------------------------------------------

%package -n	python3-%{module}
Summary:	Simple two-way ordered dictionary for Python 3
Group:		Development/Python
BuildArch:      noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python3egg(setuptools)

%description -n	python3-%{module}
TwoWayOrderedDict is a custom dictionary in which one can get the
key:value relationship but can also get the value:key relationship.
It also remembers the order in which the items were inserted and
supports almost all the features of the built-in dict.

#------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

%build
%py2_build
%py_build

%install
%py2_install
%py_install

%check
%__python2 test_twodict.py
%__python3 test_twodict.py

%files -n python2-%{module}
%doc README.md
%license LICENSE
%{python2_sitelib}/*

%files -n python3-%{module}
%doc README.md
%license LICENSE
%{python_sitelib}/*
