import axios from "axios";
import {marked} from "marked";
import Alpine from "alpinejs";
import "../css/tailwind.css"

window.axios = axios;
window.marked = marked;
window.Alpine = Alpine;

Alpine.start();
