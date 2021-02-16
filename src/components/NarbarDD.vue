<template>
    <li class="nav-item dropdown">
        <a
            class="nav-link dropdown-toggle"
            href="#"
            id="navbarDropdown"
            role="button"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
        >
            其它
        </a>
        <div
            class="dropdown-menu"
            :class="{ show: ddShow }"
            aria-labelledby="navbarDropdown"
        >
            <router-link class="dropdown-item" to="/about/gudianmingzhu">
                古典名著
            </router-link>
            <router-link class="dropdown-item" to="/about/mingrenzhuanji">
                名人传记
            </router-link>
            <router-link class="dropdown-item" to="/about/tonghua">
                儿童文学
            </router-link>
            <router-link class="dropdown-item" to="/about/gushi">
                经典故事
            </router-link>
            <router-link class="dropdown-item" to="/about/jiaoyu">
                教育励志
            </router-link>
            <router-link class="dropdown-item" to="/about/shici">
                诗词散文
            </router-link>
            <div class="dropdown-divider"></div>
            <router-link class="dropdown-item" to="/about/qtyd">
                其它阅读
            </router-link>
        </div>
    </li>
</template>
<script>
export default {
    name: "NarbarDD",
    data() {
        return {
            ddShow: false,
        };
    },
    mounted: function () {
        document.addEventListener("click", this.onClose);
    },
    methods: {
        onClose: function (event) {
            if (this.$el.contains(event.target)) {
                this.ddShow = !this.ddShow;
            } else {
                this.ddShow = false;
            }
        },
    },
    unmounted: function () {
        document.removeEventListener("click", this.onClose);
    },
};
</script>