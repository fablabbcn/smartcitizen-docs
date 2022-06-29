function toggleFullScreen() {
	sidebars = document.getElementsByClassName('md-sidebar');
	for (let sidebar of sidebars) {
		if (sidebar.classList.contains('fullscreen-mode')) {
			sidebar.classList.remove('fullscreen-mode')
		} else {
			sidebar.classList.add('fullscreen-mode')
		}
	}
	a = document.getElementsByClassName('md-tabs')[0];
	if (a.classList.contains('fullscreen-mode')) {
		a.classList.remove('fullscreen-mode')
	} else {
		a.classList.add('fullscreen-mode')
	}
};