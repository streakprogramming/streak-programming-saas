"""
Global Ops: Frontline - Development Roadmap
==========================================

This document provides a thorough textual guide for creating the "Global Ops: Frontline" Unity project.

1. Project Setup
   - Install Unity 2022.3 LTS with Universal Render Pipeline template targeting PC.
   - Create the project folder named "Global Ops: Frontline" and configure the folder structure with Assets/Scripts subdivided into Core, Player, Weapons, AI, Systems, UI.
   - Enable necessary packages: URP, Input System, TextMeshPro.
   - Configure build settings to PC (Windows) and set up quality settings for realistic visuals.

2. Scene Preparation
   - Create a "Main" scene with terrain shaped as a desert battlefield featuring multiple cover points, spawn areas, and central points of interest.
   - Bake lighting using URP, establish skybox, and ensure light probes for dynamic lighting.
   - Place empty GameObjects to mark player spawn, bot spawn points, and objective areas.

3. Core Managers
   - GameManager (singleton) handles game states: Init, Playing, Paused, GameOver. Use events for state changes.
   - CurrencyManager (singleton) tracks Coins and Tokens with methods to add/spend and events to update UI.
   - SaveSystem handles serialization of currency, settings, and progression using JSON files stored in Application.persistentDataPath.
   - UIManager (singleton) coordinates UI canvases for HUD, shop, pause, and game over screens via UnityEvents.

4. Player Systems
   - Implement a modular PlayerController using CharacterController with WASD movement, sprint toggled with Shift, jump with Space, and mouse look through Cinemachine virtual camera.
   - PlayerHealth component manages hit points, regeneration rules, and damage handling. Broadcast health changes via events.
   - WeaponHandler references equipped Weapon prefab, manages inventory, reload, switching, and interacts with CurrencyManager for purchases.

5. Weapon Architecture
   - Base Weapon class handling fire rate, recoil pattern, ammo capacity, reload time, bullet damage.
   - Projectile system using pooled Bullet prefabs with physics-based movement and collision detection applying damage to hit targets.
   - Add recoil feedback by modifying camera rotation using animation curves.

6. AI Bot Design
   - Use NavMeshAgent for pathfinding. AIController states: Idle, Patrol, Chase, Attack, Retreat.
   - Sensing through sphere overlap or Physics.Raycast to detect player.
   - BotHealth integrates with ragdoll optional death animations and drop coin rewards through CurrencyManager.
   - Weapon usage mirrors player but with AI aiming logic and configurable accuracy per wave.

7. Wave & Spawning System
   - WaveManager tracks current wave, bot count, and difficulty scaling for health, damage, and accuracy.
   - SpawnManager references bot spawn points, spawns enemies based on wave configuration, and waits until wave cleared before starting next wave.
   - Provide UI feedback for wave start/end and intermission timers.

8. Economy & Shop
   - Define ScriptableObjects for shop items (weapons, ammo, upgrades). Each includes cost, token requirements, and stat modifiers.
   - Shop UI accessible via key input or safe zone triggers; uses UnityEvents for purchase buttons connected to CurrencyManager checks.
   - Upgrades affect Weapon stats, player health, or ability cooldowns. Persist purchases via SaveSystem.

9. UI & UX
   - HUD includes crosshair, ammo counter, health bar, coin/token display, wave info.
   - Pause menu with resume, settings (audio, sensitivity), and quit options.
   - Game over screen summarizing score, coins earned, and option to restart.
   - Use TextMeshPro for text, Unity UI Toolkit or Canvas for layout.

10. Audio & Polish
   - Implement audio mixers for master, SFX, music. Link settings to SaveSystem.
   - Add weapon firing sounds, impact effects, footstep variations, ambient desert wind.
   - Include particle systems for muzzle flash, bullet impacts, and minimal post-processing for realism.

11. Testing & Optimization
   - Test wave scaling, AI behaviors, and performance in editor and builds.
   - Profile GPU/CPU usage, optimize physics layers, and reduce unnecessary updates.
   - Verify save/load consistency and currency persistence across sessions.

Use this roadmap to guide development step-by-step without auto-generating assets, maintaining clean architecture, and leveraging Unity's editor tools.
"""
