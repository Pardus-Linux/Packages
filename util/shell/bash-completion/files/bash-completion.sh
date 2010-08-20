# START bash completion -- do not remove this line
bash=${BASH_VERSION%.*}; bmajor=${bash%.*}; bminor=${bash#*.}
# interactive shell
if [ "$PS1" ]; then
	if [ $bmajor -eq 2 -a $bminor '>' 04 ] || [ $bmajor -ge 3 ]; then
		[ -f /etc/bash_completion ] && . /etc/bash_completion
		if [ -d ~/.bash_completion.d ] ; then
			for file in ~/.bash_completion.d/* ; do
				[ -f $file ] && . $file
			done
		fi
		if [ -d /usr/share/bash-completion ] ; then
			for file in /usr/share/bash-completion/* ; do
				[ -f $file ] && . $file
			done
		fi
	fi
fi
unset bash bmajor bminor
# END bash completion -- do not remove this line
