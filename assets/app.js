import "htmx.org";
import "basecoat-css/all";
import { createIcons, Sun, Moon } from "lucide";

// Register additional icons here and in the import above.
const icons = { Sun, Moon };

const initIcons = () => createIcons({ icons });

document.addEventListener("htmx:load", initIcons);
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initIcons, { once: true });
} else {
  initIcons();
}
