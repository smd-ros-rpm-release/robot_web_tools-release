Name:           ros-indigo-robot-web-tools
Version:        0.0.3
Release:        0%{?dist}
Summary:        ROS robot_web_tools package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/robot_web_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-depthcloud-encoder
Requires:       ros-indigo-interactive-marker-proxy
Requires:       ros-indigo-rosbridge-server
Requires:       ros-indigo-tf2-web-republisher
Requires:       ros-indigo-web-video-server
BuildRequires:  ros-indigo-catkin

%description
Robot Web Tools Metapackage and Top Level Launch Files

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Dec 21 2014 Russell Toris <rctoris@wpi.edu> - 0.0.3-0
- Autogenerated by Bloom

