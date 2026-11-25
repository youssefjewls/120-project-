# Atom Catcher – Bug Log

Bugs we hit while building the game and how we fixed them.
Each entry: date, who, what went wrong, why, how we fixed it.

| Date | Who | What went wrong | Why it happened | How we fixed it |
| --- | --- | --- | --- | --- |
| Nov 21 | UR | pygame window flashed open and closed instantly, with no error | `running = False` was indented at the same level as the `if`, so it ran for every event, not just the close button | Indented it inside the `if event.type == pygame.QUIT` block |
| Nov 21 | UR | Window opened but stayed blank | Forgot `pygame.display.flip()`, so the frame was drawn but never shown | Added `flip()` after drawing |
| Nov 21 | UR | `NameError` when running | Typed `pyqame` instead of `pygame` | Read the error message's last line and line number to find the typo |
| Nov 21 | UR | Timing and beaker variables placed inside the `for event` loop | Didn't realise I had messed up the order of the code | Moved setup before the loop and `dt` to the top of the loop |
| Nov 23 | UR | `UnboundLocalError` on the beaker hitbox | Function and variable were both named `beaker_hitbox`, so the variable shadowed the function | Renamed the function to `make_beaker_hitbox` |
| Nov 23 | UR | Catching loop would crash | Loop variable was named `atoms` (plural), which replaced the whole list with a single atom | Renamed the loop variable to `atom` |
| Nov 23 | UR | Catches checked before anything had moved that frame | Catching loop was at the top of the game loop | Moved it after the beaker and atoms move |
| Nov 23 | UR | Atoms counted as caught when hitting the side of the beaker | The beaker hitbox used the full beaker height | Made the hitbox only the top 20 pixels (the opening) |
| Nov 25 | UR | `SyntaxError` on `>>>streak_multiplier(0)` | Messed up where I wrote my doctests and accidently wrote them outside the docstring | Moved them inside the """ docstring |
