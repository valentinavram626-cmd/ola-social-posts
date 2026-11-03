# Reports — this directory is PUBLIC

`ola-social-posts` is a public GitHub repository. Metricool needs public
raw.githubusercontent.com URLs to fetch the post images, which is why the
repo is public and why it should stay that way.

Everything written here is therefore published on the open internet.

## Never write a person's identity in a report

Ola Accountancy is registered with the ICO as a data controller. On 3
November 2026 these reports were found to contain, for four identifiable
people: their Instagram handle, the date they contacted the firm, the
subject they wanted tax help with, and their status as a lead. That is
personal data about people who approached an accountancy firm in
confidence, published publicly. It was redacted the same day.

So, in any file committed here:

* **No handles, usernames, real names or email addresses** — not for leads,
  not for clients, not for staff, not for people who left a public comment.
  A public comment being public on YouTube does not make it ours to
  republish in a list of our leads.
* **Refer to a person by a stable label instead**: `lead-319A`, `comentariu
  IG-3`. The label is enough for Valentin to reply "approve number 1", which
  is all the report needs to do.
* **No message content that could identify someone** — a quoted sentence
  plus a date is often as identifying as a name.
* Keep the real identity where it belongs: in Metricool's inbox, in the CRM,
  or in a message to Valentin. Not in git.

## If something slips through

Redacting the file removes it from the current view, but **git history keeps
it**, and GitHub caches old commits. Removing it properly means rewriting
history and force-pushing, which Valentin must authorise — tell him rather
than doing it quietly, and say plainly that until then the old commits are
still reachable.
