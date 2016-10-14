This plugin allows to translate paths by specifying paths in a hierarchy.

Assume you have the following hierarchy of posts (default language english):
 - `about.rst`
 - `about/company.rst`
 - `about/team.rst`
 - `about/team/nikola-tesla.rst`
 - `about/team/roberto-alsina.rst`

Assuming you have set `PRETTY_URLS` to `True` and `SITE_URL` to `https://example.com`,
you can access the pages with the following URLs:
 - `https://example.com/about/`
 - `https://example.com/about/company/`
 - `https://example.com/about/team/`
 - `https://example.com/about/team/nikola-tesla/`
 - `https://example.com/about/team/roberto-alsina/`

Now assume you want to make your homepage available in more languages, say
also in german. You want the URLs for the translated posts to be:
 - `https://example.com/de/ueber/`
 - `https://example.com/de/ueber/firma/`
 - `https://example.com/de/ueber/mitarbeiter/`
 - `https://example.com/de/ueber/mitarbeiter/nikola-tesla/`
 - `https://example.com/de/ueber/mitarbeiter/roberto-alsina/`

This can be achieved with the `hierarchical_pages` plugin. If you create
translations:
 - `about.de.rst`
 - `about/company.de.rst`
 - `about/team.de.rst`
 - `about/team/nikola-tesla.de.rst`
 - `about/team/roberto-alsina.de.rst`

and use the `slug` meta data (`.. slug: xxx`) to specify the german slug,
Nikola will place the german output files so that the translations are
available under the desired URLs!

If you use plain Nikola instead, the URLs would be:
 - `https://example.com/de/ueber/`
 - `https://example.com/de/about/firma/`
 - `https://example.com/de/about/mitarbeiter/`
 - `https://example.com/de/about/team/nikola-tesla/`
 - `https://example.com/de/about/team/roberto-alsina/`

Note that this plugin requires Nikola 7.8.2. In case version 7.8.2 wasn't
released yet, please use the current master. This plugin requires
[PR 2502](https://github.com/getnikola/nikola/pull/2502) to work.
