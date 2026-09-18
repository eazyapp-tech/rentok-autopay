# Visuals

- **`../map/diagrams.md`** is the source. It has nine Mermaid diagrams, which GitHub draws on its own. Edit them there, in the same pull request as any change to the feature map.
- **`autopay-system-map.html`** is the interactive page, published at https://claude.ai/artifact/UoeBeNA6YPLcd6eSA7gL94. It shows the diagrams alongside the target, the fixed dates, the two options, the charges and a "who can do what" table you can filter by role.
- **`page-template.html`** is the same page with a `{{name}}` slot for each diagram.

## Updating the page after a diagram changes

1. Edit `map/diagrams.md`.
2. Fill the template with the diagrams, in this order: journey, states, debit2, debit1, request, money, pause, order, timeline. Escape each diagram as HTML.
3. Republish the page to the same address. In Claude Code, publish `visuals/autopay-system-map.html` with the artifact address above as `url`.
4. Only the person who first published the page can update it at that address. Anyone else creates a new page, so write the new address here.
