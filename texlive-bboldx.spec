%global tl_name bboldx
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.032
Release:	%{tl_revision}.1
Summary:	Extension of the bbold package with a Blackboard Bold alphabet
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/bboldx
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bboldx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bboldx.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Extension of bbold to a package with three weights, of which the
original is considered as light and the additions as regular and bold.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/afm
%dir %{_datadir}/texmf-dist/fonts/enc
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/bboldx
%dir %{_datadir}/texmf-dist/fonts/afm/public
%dir %{_datadir}/texmf-dist/fonts/enc/dvips
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/tex/latex/bboldx
%dir %{_datadir}/texmf-dist/fonts/afm/public/bboldx
%dir %{_datadir}/texmf-dist/fonts/enc/dvips/bboldx
%dir %{_datadir}/texmf-dist/fonts/map/dvips/bboldx
%dir %{_datadir}/texmf-dist/fonts/tfm/public/bboldx
%dir %{_datadir}/texmf-dist/fonts/type1/public/bboldx
%doc %{_datadir}/texmf-dist/doc/fonts/bboldx/Bboldx-doc.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/bboldx/Bboldx-doc.tex
%doc %{_datadir}/texmf-dist/doc/fonts/bboldx/README
%{_datadir}/texmf-dist/fonts/afm/public/bboldx/BBOLDX-Bold.afm
%{_datadir}/texmf-dist/fonts/afm/public/bboldx/BBOLDX-Regular.afm
%{_datadir}/texmf-dist/fonts/afm/public/bboldx/BBOLDX-Thin.afm
%{_datadir}/texmf-dist/fonts/enc/dvips/bboldx/bboldx.enc
%{_datadir}/texmf-dist/fonts/map/dvips/bboldx/bboldx.map
%{_datadir}/texmf-dist/fonts/tfm/public/bboldx/BBOLDX-Bold.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bboldx/BBOLDX-Regular.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bboldx/BBOLDX-Thin.tfm
%{_datadir}/texmf-dist/fonts/type1/public/bboldx/BBOLDX-Bold.pfb
%{_datadir}/texmf-dist/fonts/type1/public/bboldx/BBOLDX-Regular.pfb
%{_datadir}/texmf-dist/fonts/type1/public/bboldx/BBOLDX-Thin.pfb
%{_datadir}/texmf-dist/tex/latex/bboldx/Ubboldx.fd
%{_datadir}/texmf-dist/tex/latex/bboldx/bboldx.sty
