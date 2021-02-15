<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <router-link class="navbar-brand" to="/">Dushu</router-link>
        <button
            class="navbar-toggler"
            type="button"
            data-toggle="collapse"
            data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
            @click="toggle"
        >
            <span class="navbar-toggler-icon"></span>
        </button>

        <div
            class="collapse navbar-collapse"
            id="navbarSupportedContent"
            :class="{ show: menuOpen }"
        >
            <ul class="navbar-nav mr-auto">
                <li class="nav-item">
                    <router-link class="nav-link" to="/">全部 </router-link>
                    <span class="sr-only">(current)</span>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link" to="/about/zhongguomingzhu">
                        中国名著
                    </router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link" to="/about/waiguomingzhu">
                        外国名著
                    </router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link" to="/about/wuxiaxiaoshuo">
                        武侠小说
                    </router-link>
                </li>
                <NarbarDD />
            </ul>
            <form class="form-inline my-2 my-lg-0">
                <input
                    class="form-control mr-sm-2"
                    type="search"
                    placeholder="请输入书名"
                    aria-label="Search"
                />
                <button
                    class="btn btn-outline-success my-2 my-sm-0"
                    type="submit"
                >
                    搜索
                </button>
            </form>
        </div>
    </nav>
</template>
<style lang="scss">
.navbar {
    a.navbar-brand,
    a.navbar-brand:hover,
    a.navbar-brand:active {
        color: #42b983;
    }
}
.navbar-light .navbar-nav .nav-link.router-link-active {
    color: rgba(0, 0, 0, 1);
    &:hover,
    &:focus {
        color: rgba(0, 0, 0, 1);
    }
}
@media (max-width: 991px) {
    // .navbar-toggler {
    // }
    form.form-inline {
        justify-content: space-between;
        input.form-control {
            flex: 1;
        }
    }
}
</style>
<script>
// @ is an alias to /src
import NarbarDD from "@/components/NarbarDD.vue";
export default {
    name: "Narbar",
    components: { NarbarDD },
    data() {
        return {
            // submenus hide in mobile screen
            menuOpen: false,
        };
    },
    mounted: function () {},
    methods: {
        toggle: function () {
            this.menuOpen = !this.menuOpen;
            console.log("toggle");
        },
    },
};
</script>