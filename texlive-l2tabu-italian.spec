# revision 25218
# category Package
# catalog-ctan /info/l2tabu/italian
# catalog-date 2011-09-21 00:42:21 +0200
# catalog-license gpl
# catalog-version 1.8.4
Name:		texlive-l2tabu-italian
Version:	1.8.4
Release:	2
Summary:	Italian Translation of Obsolete packages and commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/l2tabu/italian
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-italian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-italian.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
Italian translation of the l2tabu practical guide to LaTeX2e (a
list of obsolete packages and commands).

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/l2tabu-italian/l2tabuit.pdf
%doc %{_texmfdistdir}/doc/latex/l2tabu-italian/l2tabuit.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.8.4-1
+ Revision: 770197
- texlive-l2tabu-italian
- texlive-l2tabu-italian

