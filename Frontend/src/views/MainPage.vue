<template>
  <div class="slider-container">
    <!-- 슬라이더 영역 -->
    <div class="slider" :style="{ transform: `translateX(-${currentSlide * 100}%)` }">
      <img v-for="(image, index) in images" :key="index" :src="image" alt="슬라이드 이미지" />
    </div>

    <!-- 좌우 화살표 버튼 -->
    <button class="arrow left-arrow" @click="prevSlide">❮</button>
    <button class="arrow right-arrow" @click="nextSlide">❯</button>
  </div>

  <!-- About 컴포넌트 추가 -->
  <About />
</template>

<script>
import About from "@/views/About/About.vue";

export default {
  name: "MainPage",
  components: {
    About, // 등록
  },
  data() {
    return {
      images: [
        require("@/assets/slider.jpg"),
        require("@/assets/slider2.jpg"),
        require("@/assets/slider3.jpg"),
      ],
      currentSlide: 0,
    };
  },
  mounted() {
    this.startSlider();
  },
  beforeUnmount() {
    clearInterval(this.sliderInterval);
  },
  methods: {
    startSlider() {
      this.sliderInterval = setInterval(() => {
        this.nextSlide();
      }, 5000); // 5초마다 슬라이드 변경
    },
    nextSlide() {
      this.currentSlide = (this.currentSlide + 1) % this.images.length;
    },
    prevSlide() {
      this.currentSlide =
        (this.currentSlide - 1 + this.images.length) % this.images.length;
    },
  },
};
</script>

<style scoped>
/* 컨테이너 설정 */
.slider-container {
  width: 100%;
  height: 100%; /* 슬라이더 높이 */
  overflow: hidden; /* 슬라이더 외부 이미지 숨기기 */
  position: relative;
}

/* 슬라이더 설정 */
.slider {
  display: flex;
  transition: transform 0.5s ease-in-out; /* 슬라이드 전환 애니메이션 */
  width: 100%; /* 이미지 수에 따라 변경 (100% * 이미지 개수) */
}

/* 이미지 스타일 */
.slider img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* 화살표 버튼 스타일 */
.arrow {
  position: absolute;
  top: 50%;
  transform: translateY(0%);
  background-color: rgba(225, 124, 22, 0.893);
  color: white;
  border: none;
  font-size: 24px;
  padding: 0.8% 0.8%;
  cursor: pointer;
  z-index: 10;
  border-radius: 10%;
}

/* 좌우 화살표 위치 */
.left-arrow {
  left: 10px;
}

.right-arrow {
  right: 10px;
}

/* 화살표 버튼 hover 효과 */
.arrow:hover {
  background-color: rgba(0, 0, 0, 0.8);
}
</style>
