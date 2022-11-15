Name:		texlive-bboldx
Version:	60919
Release:	1
Summary:	Extension of the bbold package with a Blackboard Bold alphabet
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bboldx
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bboldx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bboldx.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Extension of bbold to a package with three weights, of which
the original is considered as light and the additions as
regular and bold.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bboldx
%{_texmfdistdir}/fonts/type1/public/bboldx
%{_texmfdistdir}/fonts/tfm/public/bboldx
%{_texmfdistdir}/fonts/map/dvips/bboldx
%{_texmfdistdir}/fonts/enc/dvips/bboldx
%{_texmfdistdir}/fonts/afm/public/bboldx
%doc %{_texmfdistdir}/doc/fonts/bboldx

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
