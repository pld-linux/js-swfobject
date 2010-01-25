%define		ver	%(echo %{version} | tr . _)
Summary:	JavaScript Flash Player detection and embed script
Summary(pl.UTF-8):	Skrypt w JavaScripcie do wykrywania i osadzania Flash Playera
Name:		js-swfobject
Version:	2.1
Release:	2
License:	MIT
Group:		Applications/WWW
Source0:	http://swfobject.googlecode.com/files/swfobject_%{ver}.zip
# Source0-md5:	b535727aee66bac753c7e5722fd38ae2
URL:		http://code.google.com/p/swfobject/
Requires:	webapps
Requires:	webserver(alias)
Provides:	swfobject = %{version}-%{release}
Obsoletes:	swfobject
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		swfobject
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/%{_webapp}

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
%setup -q -n %{_webapp}

# Apache1 conf
cat > apache.conf <<'EOF'
Alias /js/swfobject.js %{_appdir}/swfobject.js
<Directory %{_appdir}>
	Allow from all
</Directory>
EOF

# lighttpd conf
cat > lighttpd.conf <<'EOF'
alias.url += (
    "/js/swfobject.js" => "%{_appdir}/swfobject.js",
)
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a swfobject.js $RPM_BUILD_ROOT%{_appdir}

install -d $RPM_BUILD_ROOT%{_sysconfdir}
cp -a apache.conf $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
cp -a apache.conf $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
cp -a lighttpd.conf $RPM_BUILD_ROOT%{_sysconfdir}/lighttpd.conf

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%triggerin -- lighttpd
%webapp_register lighttpd %{_webapp}

%triggerun -- lighttpd
%webapp_unregister lighttpd %{_webapp}

%files
%defattr(644,root,root,755)
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lighttpd.conf
%{_appdir}
