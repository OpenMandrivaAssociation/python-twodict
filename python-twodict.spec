%define module	twodict

Name:		python-%{module}
Version:	1.2
Release:	4
Summary:	Simple two-way ordered dictionary for Python
License:	Public Domain
Group:		Development/Python
Url:		https://github.com/MrS0m30n3/twodict
Source0:	https://files.pythonhosted.org/packages/source/t/twodict/%{module}-%{version}.tar.gz
Patch0:   fix-build-python310.patch
BuildArch:      noarch

%description
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
BuildRequires:	python3dist(setuptools)

%description -n	python3-%{module}
TwoWayOrderedDict is a custom dictionary in which one can get the
key:value relationship but can also get the value:key relationship.
It also remembers the order in which the items were inserted and
supports almost all the features of the built-in dict.

#------------------------------------------------

%prep
%setup -q -n %{module}-%{version}
%autopatch -p1

%build
%py_build

%install
%py_install

%files -n python3-%{module}
%doc README.md
%license LICENSE
%{python_sitelib}/*
