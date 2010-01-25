%define		ver	%(echo %{version} | tr . _)
Summary:	JavaScript Flash Player detection and embed script
Summary(pl.UTF-8):	Skrypt w JavaScripcie do wykrywania i osadzania Flash Playera
Name:		js-swfobject
Version:	2.1
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	http://swfobject.googlecode.com/files/swfobject_%{ver}.zip
# Source0-md5:	b535727aee66bac753c7e5722fd38ae2
URL:		http://code.google.com/p/swfobject/
Provides:	swfobject = %{version}-%{release}
Obsoletes:	swfobject
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/swfobject

%description
SWFObject is a small JavaScript file used for embedding Adobe Flash
content. The script can detect the Flash plug-in in all major web
browsers (on Mac and PC) and is designed to make embedding Flash
movies as easy as possible. It is also very search engine friendly,
degrades gracefully, can be used in valid HTML and XHTML 1.0
documents, and is forward compatible, so it should work for years to
come.

%description -l pl.UTF-8
SWFObject to mały plik w JavaScripcie służący do osadzania treści
Adobe Flash. Skrypt potrafi wykryć wtyczkę Flash we wszystkich
popularnych przeglądarkach (na Macu i PC) i jest zaprojektowany do jak
najłatwiejszego osadzania filmów we Flashu. Jest także przyjazny dla
silników wyszukiwarek, dobrze się degraduje, może być używany w
poprawnych dokumentach HTML oraz XHTML 1.0 i jest zgodny w przód, więc
powinien działać jeszcze przez wiele lat.

%prep
%setup -q -n swfobject

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a swfobject.js $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
