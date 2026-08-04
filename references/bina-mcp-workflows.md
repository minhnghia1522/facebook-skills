# Bina Social Poster MCP workflows

Use this reference whenever Bina Social Poster MCP tools are available in the
agent host. Skills provide the writing judgment and approval flow. MCP provides
the user's pages, media, posts, schedules, and write actions.

## Read before drafting or writing

1. Call `list_pages` to identify connected Facebook Pages and their status.
2. Call `list_media` when the request mentions an image or video, or when a
   post already has selected media.
3. Call `list_posts` or `get_post` when the user asks to learn from existing
   posts, revise a saved draft, or inspect a post's attached media.

Do not guess a page ID, media UUID, post UUID, or current post version.

## Write after explicit approval

### Create a draft

Call `create_post` with:

- `post_type`: `TEXT`, `IMAGE`, `VIDEO`, or `LINK`
- approved `content`
- `link_url` only for a link post
- `media_ids` only for user-owned media selected from `list_media`
- a fresh `idempotency_key`

`create_post` creates a `DRAFT`; it does not publish to Facebook.

### Update an existing draft

Call `update_post` with the post UUID and the exact `version` returned by
`get_post`. If the version conflicts, re-read the post and show the user the
new content before retrying.

### Schedule a post

Call `create_scheduled_post` only after confirming the exact Page and time with
the user. Pass one or more targets with `platform_page_id`, `scheduled_at` in
RFC3339, `timezone`, and an optional `content_override`. The server requires a
time at least five minutes in the future and creates the post in `READY` status.
Use a fresh `idempotency_key` for the complete request and do not blindly retry
after an unknown result.

### Inspect a schedule

Use `list_schedules` or `get_schedule` to report scheduled, queued, publishing,
published, failed, or cancelled state. Include the latest error message when a
target failed.

### Destructive actions

Call `delete_post` only when the user explicitly asks to archive a post. Warn
that it also cancels unexecuted target schedules and cannot remove a post that
is already publishing or published.

## Approval contract

Always show the complete final text, target Page, post type, media, schedule,
timezone, and any link before a write tool call. Treat "draft", "save", and
"prepare" as `create_post`. Treat "publish now" as a draft plus the user's
normal Bina publishing flow unless the MCP server exposes an explicit immediate
target operation. Treat "schedule" as `create_scheduled_post`.

If the MCP server is unavailable, return a copy-paste block and say that no
external write was performed. Never ask the user to paste an MCP API key into
the conversation or commit it to this bundle.
