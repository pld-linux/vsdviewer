Summary:	VSDviewer - Viewer for Visio VSD/VSS files.
Name:		vsdviewer
Version:	0.0.13	
Release:	0.1
License:	GPL
Group:		Applications
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	26a40332cb652e554578a228d9613897
URL:		http://www.sk1project.org/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Viewer for Visio VSD/VSS files.

%description -l pl.UTF-8
Przeglądarka dla plików pakietu Visio VSD/VSS.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_bindir}}
install *.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install *.png $RPM_BUILD_ROOT%{_datadir}/%{name}
install vsdviewer $RPM_BUILD_ROOT%{_datadir}/%{name}
ln -s %{_datadir}/%{name}/vsdviewer $RPM_BUILD_ROOT%{_bindir}/vsdviewer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.p*
%attr(755,root,root) %{_datadir}/%{name}/vsdviewer
