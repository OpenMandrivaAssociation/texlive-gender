Name:		texlive-gender
Version:	36464
Release:	2
Summary:	Gender neutrality for languages with grammatical gender
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gender
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gender.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gender.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gender.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Many languages -- like German or French -- use masculine and
feminine grammatical genders. There are many ideas how to
promote gender neutrality in those languages. The gender
package uses alternately masculine and feminine forms. It is
also possible to use just one form out of a template.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/gender
%{_texmfdistdir}/tex/latex/gender
%doc %{_texmfdistdir}/doc/latex/gender

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
