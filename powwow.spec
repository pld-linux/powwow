Summary:	Powwow
Name:		powwow
Version:	1.2.0
Release:	0
License:	GPL
Group:		Games
Source0:	ftp://Linuz.sns.it/pub/Linux/ext-pack/%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A client to play MUDs. It has a lot of features that people commonly miss 
with telnet: just to say two, line editing and aliases. Developed on MUME 
mud. Too many people contributed to list them all here.

%prep
%setup -q

%build
%{__make} CC=gcc CDEFS="$RPM_OPT_FLAGS -DUSE_REGEXP" LDFLAGS="-lncurses" powwow

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
