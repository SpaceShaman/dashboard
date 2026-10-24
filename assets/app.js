import "htmx.org";
import "basecoat-css/all";
import { createIcons, icons } from "lucide";

const initIcons = () => createIcons({ icons });

document.addEventListener("htmx:load", initIcons);
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initIcons, { once: true });
} else {
  initIcons();
}
