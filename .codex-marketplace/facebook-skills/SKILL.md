---
name: facebook-marketing
description: Plan, draft, audit, and publish posts for a Facebook Page. Use when the user wants to write a short punchy Page post or a longer story post, remove AI tells from a draft, reverse-engineer the hook from a high-share Page post, draft replies to comments on their Page, or plan a week of Facebook Page content. When Bina Social Poster MCP tools are available, use them for page, media, post, and schedule operations after explicit approval. Not for personal profiles.
---

# Facebook Pages Marketing Skills

A bundle of 8 focused skills for Facebook Page content ops in 2026. Each skill is
single-purpose, follows the draft then approval then write pattern, and uses
Bina Social Poster MCP for user-scoped page and post operations when available.

## When to use this bundle

- **Writing a short punchy Page post or a longer story post** -> use `fb-post-writer`
- **Removing AI tells from a draft, or auditing it before posting** -> use `fb-humanizer` (rewrite plus `--mode audit` pre-publish review, which folds in the post-audit sub-tool)
- **Repurposing a LinkedIn post, X thread, blog, or newsletter into a native Page post** -> use `fb-repurposer`
- **Reverse-engineering the hook from a high-share Page post** -> use `fb-hook-extractor`
- **Drafting replies to comments on your Page's posts** -> use `fb-engagement-drafter`
- **Planning a week of Facebook Page content** -> use `fb-content-planner`
- **Auditing and rewriting the Page itself (name, cover, About, CTA button, pinned post)** -> use `fb-page-optimizer`
- **Reading a Page's stats (yours or a competitor's) or the commenters on a post from real data** -> use `fb-audience-insights`

## Core pattern

Every action-taking skill follows three steps:

1. **Read context.** If Bina MCP is available, call `list_pages`, and call
   `list_media`, `list_posts`, or `get_post` when the request needs those
   resources. If the user gives a Facebook Page post URL, use
   `lib/url_parser.py` to extract the page and post id.
2. **Draft the content.** The skill applies Facebook hook
   formulas, the under-80-char engagement sweet spot, timing, voice rules,
   ranking heuristics) and shows the draft to the user.
3. **Wait for approval.** The user replies "post", "yes", or suggests edits.
   Only after explicit approval does the skill call a Bina MCP write tool.

## Prerequisites

**Three tiers - pick one.**

### Tier 0 - Draft only (default, no setup)

The skills work out of the box. No API keys, no signup. Every approved draft is
returned as a copy-paste block with the target Facebook Page URL. Great for
trying the skills before committing to any backend.

### Tier 1 - Bina Social Poster MCP

Configure the Bina MCP server in the agent host, then expose its tools to the
conversation. The skill uses `list_pages`, `list_media`, `list_posts`, and
`get_post` for context, `create_post` for drafts, `update_post` for revisions,
and `create_scheduled_post` for approved schedules. MCP authentication stays in
the host configuration and never belongs in this repository.

### Tier 2 - Draft-only fallback

Without MCP tools, the skills still produce an approval card and a copy-paste
block. They must not claim that a post was created or scheduled.

### Note on comment replies

The current Bina MCP tool set has no comment-reply operation. So
`fb-engagement-drafter` returns approved replies as copy-paste blocks for you to
post as replies in Facebook or Meta Business Suite yourself. Page posts and
schedules use the Bina MCP tools described in `references/bina-mcp-workflows.md`.

## Voice rules (baked into every skill)

1. No em dashes (`—`), en dashes, or double dashes. Biggest AI tell.
2. Use `..` as a soft pause when rhythm calls for it.
3. Capitalize all personal, company, and product names. Lowercase a brand reads
   as careless.
4. Write for a Page (a warm business voice), not a personal profile and not a
   faceless corporate account.
5. Avoid AI vocabulary: `leverage`, `fundamentally`, `streamline`, `harness`,
   `delve`, `unlock`, `foster`.
6. Specific numbers beat adjectives. 2.4x beats "way better".
7. One idea per post. Two ideas means two posts.
8. Lead short. Posts under 80 chars get a reported ~66% engagement lift.
9. The first line carries everything (Facebook folds longer posts behind "See more").
10. 0-2 hashtags, 0-2 emoji, and only when each earns its place.

(Canonical reference: `references/voice-rules.md`. See also
`references/hook-formulas.md` and `references/algorithm-heuristics.md`.)

## How Facebook Page URLs map

| URL shape | Parsed to |
|---|---|
| `https://www.facebook.com/PAGE/posts/ID` | page + post_id, type `post` |
| `https://www.facebook.com/permalink.php?story_fbid=ID&id=PAGEID` | post_id + page, type `post` |
| `https://www.facebook.com/watch/?v=ID` | post_id (video), type `post` |
| `https://www.facebook.com/share/p/TOKEN/` | share_token, type `share` (ids hidden) |
| `https://www.facebook.com/PAGE` | page, type `profile` |
| `https://fb.com/PAGE` | normalized to www.facebook.com |

`lib/url_parser.parse_facebook_url(url)` returns `{page, post_id, share_token,
url_type, canonical_url}`. A `share/p/` link hides the page and post ids behind
an opaque token, so the parser flags it and the skill asks you to paste the post
text.

## Known gotchas

- **The under-80-char sweet spot is real.** Posts under 80 characters get a
  reported ~66% engagement lift. Lead short; go long only on purpose.
- **Text-only Page posts are fully supported**, unlike Instagram, TikTok, and
  YouTube. You do not need media to post.
- **External links suppress organic reach.** A link post still drives traffic but
  reaches fewer people than a native text, photo, or video post.
- **Pages only, never personal profiles.** This bundle targets connected Facebook
  Pages, not personal profiles.
- **MCP context is user-scoped.** Use the pages and media returned for the
  current MCP user. Never invent IDs or reuse another user's identifiers.
- **No Facebook comment endpoint.** Comment replies are draft-only by design; the
  engagement drafter returns a copy-paste block.

## Resources

- `references/bina-mcp-workflows.md` - MCP tool mapping and approval contract
- `lib/url_parser.py` - Facebook Page URL to page/post-id parser

## Acknowledgments

Writing is powered by the skill bundle; page and schedule writes use Bina Social
Poster MCP when the host exposes it.
