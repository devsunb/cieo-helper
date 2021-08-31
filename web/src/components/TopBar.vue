<template>
    <nav class="navbar navbar-expand-lg fixed-top navbar-dark bg-dark">
        <a class="navbar-brand" href="#">CIEO Helper</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggler" aria-controls="navbarToggler" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarToggler">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item">
                    <router-link class="nav-link" exact-active-class="active" :to="{name:'MainPage'}">Home</router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link" exact-active-class="active" :to="{name:'CoreTheorem'}">핵심정리</router-link>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">문제풀이</a>
                    <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                        <!-- <a class="dropdown-item" href="#">필기 기출문제</a>
                        <div class="dropdown-divider"></div>
                        <a class="dropdown-item" href="#">실기 기출문제</a> -->
                        <router-link class="dropdown-item" exact-active-class="active" :to="{name:'CrammingCommand'}">명령어 벼락치기</router-link>
                    </div>
                </li>
            </ul>
            <form class="form-inline my-2 my-lg-0 search-form">
                <input class="search-input" type="search" placeholder="Search...">
                <button class="search-btn my-2 my-sm-0" type="submit"><i class="fas fa-search"></i></button>
            </form>
        </div>
    </nav>
</template>

<script>
export default {
    name: "top-bar"
};
</script>

<style scoped>
*:focus {
    outline: none;
}
.search-form {
    width: 400px;
}
.search-input {
    width: 92%;
    background-color: transparent;
    color: white;
    border: 0;
    border-radius: 0;
    border-bottom: 1px solid white;
}
.search-btn {
    width: 8%;
    background-color: transparent;
    color: white;
    border: 0;
    border-radius: 0;
    border-bottom: 1px solid white;
    cursor: pointer;
}

@media (max-width: 991px) {
    .search-form {
        width: 100%;
    }
}
</style>
