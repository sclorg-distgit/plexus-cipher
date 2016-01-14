%global pkg_name plexus-cipher
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.7
Release:        5.11%{?dist}
Summary:        Plexus Cipher: encryption/decryption Component

License:        ASL 2.0
# project moved to GitHub and it looks like there is no official website anymore
URL:            https://github.com/sonatype/plexus-cipher
# git clone https://github.com/sonatype/plexus-cipher.git
# cd plexus-cipher/
# note this is version 1.7 + our patches which were incorporated by upstream maintainer
# git archive --format tar --prefix=plexus-cipher-1.7/ 0cff29e6b2e | gzip -9 > plexus-cipher-1.7.tar.gz
Source0:        %{pkg_name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: %{?scl_prefix}maven-plugin-plugin
BuildRequires: %{?scl_prefix}maven-resources-plugin
BuildRequires: %{?scl_prefix}maven-doxia-sitetools
BuildRequires: %{?scl_prefix}forge-parent
BuildRequires: %{?scl_prefix}spice-parent
BuildRequires: %{?scl_prefix}plexus-containers-component-metadata
BuildRequires: %{?scl_prefix_java_common}junit
BuildRequires: %{?scl_prefix}maven-reporting-impl
BuildRequires: %{?scl_prefix}plexus-digest
BuildRequires: %{?scl_prefix}sisu-maven-plugin
BuildRequires: %{?scl_prefix}sisu-inject-bean
BuildRequires: %{?scl_prefix}cdi-api



%description
Plexus Cipher: encryption/decryption Component

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.


%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x

# replace %{version}-SNAPSHOT with %{version}
%pom_xpath_replace pom:project/pom:version "<version>%{version}</version>"

# plexus-cipher uses @Typed annotation
%pom_add_dep javax.enterprise:cdi-api:1.0:provided

%mvn_file : plexus/%{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/plexus
%dir %{_javadir}/plexus
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Fri Jan 16 2015 Michal Srb <msrb@redhat.com> - 1.7-5.11
- Fix directory ownership

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.7-5.10
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.7-5.9
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-5.8
- Mass rebuild 2014-05-26

* Fri Mar 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-5.7
- Add dependency on cdi-api

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-5.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-5.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-5.4
- Remove requires on java

* Fri Feb 14 2014 Michael Simacek <msimacek@redhat.com> - 1.7-5.3
- SCL-ize BR

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-5.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-5.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.7-5
- Mass rebuild 2013-12-27

* Mon Aug 19 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.7-4
- Migrate away from mvn-rpmbuild (#997451)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-3
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Mar 13 2013 Michal Srb <msrb@redhat.com> - 1.7-1
- Update to upstream version 1.7

* Thu Feb 21 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-15
- Reemove BR: plexus-container-default

* Fri Feb 08 2013 Michal Srb <msrb@redhat.com> - 1.5-14
- Remove unnecessary dependency on plexus-containers (#908586)

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.5-13
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 02 2013 Michal Srb <msrb@redhat.com> - 1.5-12
- Fixed URL (Resolves: #880322)

* Tue Nov 27 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-11
- Improve randomness of PBECipher
- Resolves: rhbz#880279

* Mon Nov 26 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-10
- Remove duplicated NOTICE file

* Mon Nov 26 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.5-9
- Add ASL 2.0 text and install NOTICE file

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Jaromir Capik <jcapik@redhat.com> - 1.5-6
- Migration from plexus-maven-plugin to plexus-containers-component-metadata
- Minor spec file changes according to the latest guidelines

* Fri Jun 3 2011 Alexander Kurtakov <akurtako@redhat.com> 1.5-5
- Do not require maven2.
- Build with maven (v. 3) by default.
- drop obsoleted parts of the spec.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 01 2010 Hui Wang <huwang@redhat.com> - 1.5-3
- Add NOTICE.text
- Fix URL
- Fix direction of install pom

* Sun May 23 2010 Hui Wang <huwang@redhat.com> - 1.5-2
- Correct URL

* Tue May 18 2010 Hui Wang <huwang@redhat.com> - 1.5-1
- Initial version of the package
