# Public Code Category Instructions

## Scope and Inheritance

Read `../AGENTS.md`, relevant `../CONVENTIONS.md` sections, and the project's
`AGENTS.md` and README. This category instruction belongs to `workspace-meta`.
Project contents belong to their own repositories, where a repository exists.

## Role and Structure

- This category holds code intended for external use, including local/private
  release candidates. Its name does not establish public visibility or release.
- Keep source, tests, examples, public documentation, dependency metadata,
  license, and third-party notices in the project's established layout.
- Ordinary setup and tests must work without private sibling repositories.
  Optional artifact downloads must have a documented access/provenance contract.
- Preserve documented APIs and compatibility names. Use Git history for edits
  and explicit software release versions for intentional API changes.

## Release Boundary

- Keep unpublished manuscripts, personal notes, confidential reviews, private
  paths, credentials, and local experiment dumps outside public commits.
- Generated outputs stay ignored unless explicitly approved as a public data
  artifact with provenance, licensing, and reproducibility information.
- Do not infer a license from this category or replace existing attribution.
- Inspect actual remote visibility and outgoing commits before an authorized
  push. A shared research branch is visible when its remote is public.
- A code package without its own Git metadata remains a local package; never
  stage it into `workspace-meta` or initialize/publish it implicitly.
