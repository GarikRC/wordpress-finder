Wordpress finder
================
Trivial, dirty Python hack to go through /home (yep - hardcoded in the code) and try to find all of the Wordpress instances you've got there while printing their versions.

Even so lame, pretty handy to have this running from cron to tell you when someone is lazy and doesn't keep their Wordpress updated.

Planned features:
  1. Parametrise the directory
  1. More verbose output (like Wordpress URL or name)
  1. Ability to mail owners automatically every night; hopefully if they get hassled bad enough it'll make them upgrade their installations
  1. Anything else that you think could be useful
