%define 	module	rbtools
Summary:	Tools for use with ReviewBoard
Name:		python-%{module}
Version:	0.4.3
Release:	1
License:	MIT
Group:		Applications/Networking
Source0:	http://downloads.reviewboard.org/releases/RBTools/0.4/RBTools-%{version}.tar.gz
# Source0-md5:	fc76cbe3a9f023a012966577bdd300d6
Patch1001:	no_ez_setup.patch
URL:		http://www.review-board.org/
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-setuptools
Requires:	python-simplejson
Obsoletes:	RBTools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RBTools provides client tools for interacting with a ReviewBoard
code-review server.

%prep
%setup -q -n RBTools-%{version}
%{__rm} -r RBTools*.egg-info
%patch1001 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

# While %{_bindir}/post-review also exists for this purpose,
# it is still sensible to make postreview.py executable
install -p rbtools/postreview.py $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/postreview.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/post-review
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/RBTools*.egg-info/
