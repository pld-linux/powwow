Summary:	powwow - MUD client
Summary(pl):	powwow - klient MUD
Name:		powwow
Version:	1.2.0
Release:	0
License:	GPL
Group:		Applications/Games
Source0:	ftp://Linuz.sns.it/pub/Linux/ext-pack/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-time.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A client to play MUDs. It has a lot of features that people commonly
miss with telnet: just to say two, line editing and aliases. Developed
on MUME mud. Too many people contributed to list them all here.

%description -l pl
Klient do gry w MUD-y. Ma wiele mo¿liwo¶ci, których brakuje ludziom
u¿ywaj±cym telneta: m.in. edycja linii i aliasy. Rozwijany z mudem
MUME.

%prep
%setup -q
%patch0 -p1

%build
%{__make} CC="%{__cc}" CDEFS="%{rpmcflags} -DUSE_REGEXP" LDFLAGS="-lncurses %{rpmldflags}" powwow

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
