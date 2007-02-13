Summary:	powwow - MUD client
Summary(pl.UTF-8):	powwow - klient MUD
Name:		powwow
Version:	1.2.5
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://linuz.sns.it/~max/powwow/%{name}-%{version}.tar.gz
# Source0-md5:	704b94581b396d6ea17c00a5d1149ae1
URL:		http://linuz.sns.it/~max/powwow/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A client to play MUDs. It has a lot of features that people commonly
miss with telnet: just to say two, line editing and aliases. Developed
on MUME mud. Too many people contributed to list them all here.

%description -l pl.UTF-8
Klient do gry w MUD-y. Ma wiele możliwości, których brakuje ludziom
używającym telneta: m.in. edycja linii i aliasy. Rozwijany z mudem
MUME.

%prep
%setup -q

%build
%{__make} powwow movie_play movie2ascii follow catrw \
	CC="%{__cc}" \
	CDEFS="%{rpmcflags} -DUSE_REGEXP" \
	LDFLAGS="-lncurses %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6}

install powwow movie{,2ascii,_play} make_it follow catrw $RPM_BUILD_ROOT%{_bindir}
install powwow.6 $RPM_BUILD_ROOT%{_mandir}/man6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README{,.follow,.term} Changelog Compile.how Config.demo Hacking powwow.{doc,help}
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/powwow*
