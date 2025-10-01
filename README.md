# The Last Haven: Idle Refuge

> **Status**: In Development  
> **Genre**: Idle/Incremental Game  
> **Platform**: Desktop (Python/Pygame)  
> **Inspiration**: Melvor Idle

## 🎯 Project Status

- [ ] **Naming**: Still needs a final name
- [ ] **Documentation**: Heavy notes/learning material is documented in a Notion doc with detailed explanations
- [ ] **Core Gameplay**: Basic idle mechanics implemented
- [x] **UI/UX**: Menu system and basic interface complete
- [ ] **Save System**: Basic save functionality in place
- [ ] **Content**: 3 active skills + 6 passive skills framework established

## 📖 Overview

**The Last Haven: Idle Refuge** is an incremental/idle game inspired by Melvor Idle, built as a learning project using Python and Pygame. The game focuses on resource management and skill progression in a post-apocalyptic survival setting.

### 🎮 Gameplay Mechanics

**Active Skills** (Player must actively engage):
- **Foraging**: Gather natural resources from the environment
- **Hunting**: Track and hunt wildlife for food and materials  
- **Scavenging**: Search abandoned areas for useful items

*Note: Players can only perform one active skill at a time*

**Passive Skills** (Automated progression with resource investment):
- **Cooking**: Process raw materials into better food items
- **Engineering**: Craft tools and improve equipment
- **Legacy**: Build lasting improvements to your refuge
- **Medicine**: Develop healing items and medical knowledge
- **Fortification**: Strengthen your base against threats
- **Community**: Build relationships and unlock group benefits

### 🛠️ Technical Details

- **Language**: Python 3.x
- **Framework**: Pygame for graphics and game loop
- **Architecture**: Modular design with separate entities, menus, and services
- **Save System**: Local file-based save functionality
- **UI**: Custom menu system with reusable components

## Features

- Menu Select
- Customizable Buttons
- Temp Inventory
- Scavenging
- A toggle to gather a group of resources

## Project Structure

```
The-Last-Haven-Idle-Refuge/
├── Entities/
│   ├── Button.py
│   ├── GameState.py
│   ├── Player.py
│   └── Scavenging.py
├── Menus/
│   ├── Core/
│   │   ├── DefaultMenu.py
│   │   ├── InventoryMenu.py
│   │   └── ShopMenu.py
│   └── Skills/
│       ├── CommunityMenu.py
│       ├── CookingMenu.py
│       ├── EngineeringMenu.py
│       ├── ForagingMenu.py
│       ├── FortificationMenu.py
│       ├── HuntingMenu.py
│       ├── LegacyMenu.py
│       ├── MedicineMenu.py
│       └── ScavengingMenu.py
├── Services/
│   ├── Mutator.py
│   └── SaveFunction.py
├── Main.py
├── README.md
└── .gitignore
```