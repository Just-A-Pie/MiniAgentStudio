# Social Scene Map Editing & Simulation Playback Tool

**The major author of this tool is Shunqiang Mao, supervised by **[**Tianxing He**](https://cloudygoose.github.io/)**. This project was completed during an internship at Shanghai Qi Zhi Institute.**

This project offers two usage phases:

- **Map Editor** – Visually place, move, delete buildings & objects; manage *container* relationships and optional attributes; persist global layer CSV grids plus placed-instance JSON.
- **Simulation** – Load time‑series simulation data (multi‑step agent states + `noteworthy` events), play step by step, inspect each agent’s current state and activity history.

You only need a **Map Folder** (map resources) and a **Sim Folder** (simulation data). Sample folders are included at the project root so you can try it immediately.

---

## Ultra‑Brief Overview

- **Startup Input**: In the startup scene manually enter absolute paths. Map Editor needs only *Map Folder*; Simulation needs *Map Folder* + *Sim Folder*.
- **Map Editor – 5 Core Actions**: Enter path → enter editor → select resource in toolbar → place / move / delete / edit attributes → save (writes global CSV + instance JSON).
- **Simulation – 4 Core Actions**: Enter both paths → enter playback → play / change speed / jump step → inspect agents & multi‑line `noteworthy` events + histories.
- **Minimal Resource Set**: `Map Folder` contains `map/` (background + global CSV + instance JSON), `buildings/`, `objects/`; `Sim Folder` only needs `records_for_sim.json`.
- **Event Format Quick View**: Each timestamp object in `records_for_sim.json`: `{ "AgentName": { ...state... }, "noteworthy": [{"event": "...", "people": ["A","B"]}, ...] }`.

---

## Table of Contents

1. [Quick Start With Provided Templates](#quick-start-with-provided-templates)
2. [Folder Structure & Resources](#folder-structure--resources)
3. [Feature Overview — Map Editor](#feature-overview--map-editor)
4. [Feature Overview — Simulation](#feature-overview--simulation)
5. [Data Format Cheat Sheet](#data-format-cheat-sheet)

---

## Quick Start With Provided Templates

The project root ships two ready‑to‑use example folders (names may vary):

```
SampleMap/   ← use as Map Folder
SampleSim/   ← use as Sim Folder
```

> **All paths must be entered manually as absolute paths.**\
> Map Editor launch requires only the **Map Folder**; Simulation launch requires **both** absolute paths.

### Launching the Map Editor

1. Open Unity and run the startup scene.
2. In the **Map Folder** input field, enter the absolute path to `SampleMap` (e.g. `C:\Project\SampleMap` or `/Users/you/Project/SampleMap`).
3. (No Sim Folder needed for the editor.)
4. Click **Map Editor** to enter the editing interface.
5. Place / move / delete / modify attributes; press **Save** to write updates (overwrites global CSV in `map/maze/` and instance JSON in `map/map_data/`).

### Launching the Simulation Playback

1. Run the startup scene.
2. **Map Folder**: absolute path to the desired `SampleMap` (preferably the one you just edited/saved).
3. **Sim Folder**: absolute path to `SampleSim`.
4. Click **Simulation** to enter playback UI.
5. Use play / pause / jump / speed controls to view agent positions, activities, `noteworthy` event lines, and histories.

> To see your freshly edited map inside Simulation, ensure the Simulation startup uses the *same* Map Folder you saved in the editor.

---

## Folder Structure & Resources

### Map Folder (Example Structure)

```
SampleMap/
├─ map/
│  ├─ texture.png              # Global background image
│  ├─ maze_meta_info.json      # Global map metadata (dimensions, etc.)
│  ├─ maze/                    # Global CSV layers (sector / arena / game_object / collision ...)
│  └─ map_data/
│     ├─ buildings_data.json   # Placed building instances
│     └─ objects_data.json     # Placed object instances
├─ buildings/
│  └─ HouseA/
│      ├─ texture.png
│      └─ maze_meta_info.json  # typeId / footprint (width × height in tiles)
└─ objects/
   └─ ChairA/
       ├─ texture.png
       └─ maze_meta_info.json
```

**Load Process**

- On editor start, each subfolder under `buildings/` & `objects/` is scanned; `maze_meta_info.json` + `texture.png` become toolbar entries.
- **Save** rewrites:
  - Global CSV under `map/maze/`
  - Placed instance JSON under `map/map_data/` (`buildings_data.json`, `objects_data.json`).

### Sim Folder (Example Structure)

```
SampleSim/
└─ records_for_sim.json
```

- Top-level keys: timestamps (ISO 8601 or legacy `HH_MM_SS am/pm`).
- Each timestamp value: several agent objects + optional `noteworthy` array.

---

## Feature Overview — Map Editor

| Feature             | Description                                                                                |
| ------------------- | ------------------------------------------------------------------------------------------ |
| Item Placement      | Select a toolbar entry then left‑click grid (auto snap).                                   |
| Item Move           | Open item popup → **Move** → pick new grid cell.                                           |
| Item Deletion       | Popup **Delete**; if a container, deletes its children.                                    |
| Containers          | Enable `container` attribute then add children; parent shows small logo badge.             |
| Add Child Items     | Press the “+” button in the container attribute row (children have no map grid footprint). |
| Optional Attributes | Example: `quantity`, `container`; disabled attributes are omitted from save files.         |
| Grid Overlay        | Button cycles: none → Sector → Arena (colored cells & labels).                             |
| Item Popup          | View / edit name & attributes; move / delete actions.                                      |
| Save / Reset        | Save writes CSV + JSON; reset returns to last saved state.                                 |
| View Interaction    | Right‑drag pan; scroll zoom; hover shows tile coords; toggle container logos.              |

---

## Feature Overview — Simulation

| Feature           | Description                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------- |
| Step Playback     | Play / pause; jump to step; multiple speeds (1×–64×).                                                   |
| Smooth Movement   | Interpolated motion between discrete step grid positions.                                               |
| Noteworthy Events | If present, multi‑line: `[Person1, Person2] Event text`.                                                |
| Agent Info        | Hover or click to see grid coords, current activity, location, filtered bag (irrelevant items removed). |
| Activity History  | “History” view lists up to the latest 100 activities (newest first).                                    |
| Item Info         | Hover/click map items for name, category, coordinates, attributes.                                      |
| Pin Highlight     | Click agent or item to pin & highlight; click again to unpin.                                           |

---

## Data Format Cheat Sheet

### `records_for_sim.json` (Simplified Example)

```jsonc
{
  "2024-06-01T08:00:00": {
    "Alice": {
      "name": "Alice",
      "activity": "Preparing breakfast",
      "location": "Kitchen",
      "bag": ["bread", "milk"],
      "curr_tile": [5, 7],
      "short_activity": "cook",
      "walkingSpriteSheetName": "Alice"
    },
    "Bob": { /* ... another agent ... */ },
    "noteworthy": [
      { "event": "Picking up blankets from their beds", "people": ["Klaus Mueller", "Maria Lopez"] },
      { "event": "Traveling to individual locations for items", "people": ["Isabella Rodriguez", "Klaus Mueller", "Maria Lopez"] }
    ]
  },
  "2024-06-01T08:05:00": { /* next timestep ... */ }
}
```

**Notes**

- Each timestamp object merges agent states and a `noteworthy` array.
- `bag` supports either `["item"]` or `[["item","uuid"], ...]` — internally normalized to plain strings.
- Agents without `activity` fallback to `short_activity`; if both missing an idle marker is shown.

### Placed Items JSON (`buildings_data.json` / `objects_data.json`)

```jsonc
{
  "buildings": [
    {
      "uniqueId": "uuid-1",
      "typeId": 10,
      "x": 12,
      "y": 4,
      "itemName": "HouseA",
      "attributes": [ { "key": "quantity", "value": "2" }, { "key": "container", "value": "childUuid1,childUuid2" } ]
    }
  ]
}
```

- Child objects (if any) can exist with grid `x = -1`, `y = -1` (managed only through a parent container).

---



