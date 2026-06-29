const canvas = document.querySelector("#biome-canvas");
const ctx = canvas.getContext("2d");
const supportModal = document.querySelector("#support-modal");
const supportOpenButtons = document.querySelectorAll("[data-support-open]");
const supportCloseButtons = document.querySelectorAll("[data-support-close]");

const palette = ["#2f6b46", "#2d6f89", "#a9552f", "#c49a44", "#d7dccb"];
const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

let width = 0;
let height = 0;
let points = [];
let animationFrame = 0;
let lastSupportTrigger = null;

function resize() {
  const pixelRatio = Math.min(window.devicePixelRatio || 1, 2);
  width = canvas.clientWidth;
  height = canvas.clientHeight;
  canvas.width = Math.floor(width * pixelRatio);
  canvas.height = Math.floor(height * pixelRatio);
  ctx.setTransform(pixelRatio, 0, 0, pixelRatio, 0, 0);
  points = createPoints();
  draw(0);
}

function createPoints() {
  const count = Math.max(42, Math.floor((width * height) / 22000));
  return Array.from({ length: count }, (_, index) => {
    const angle = (index / count) * Math.PI * 2;
    const radius = 0.18 + ((index * 37) % 100) / 260;
    return {
      x: width * (0.55 + Math.cos(angle) * radius * 0.7) + Math.sin(index) * 70,
      y: height * (0.52 + Math.sin(angle) * radius) + Math.cos(index * 1.7) * 48,
      baseX: width * (0.55 + Math.cos(angle) * radius * 0.7),
      baseY: height * (0.52 + Math.sin(angle) * radius),
      color: palette[index % palette.length],
      size: 1.4 + (index % 5) * 0.55,
      phase: index * 0.31,
    };
  });
}

function drawMapSilhouette(time) {
  ctx.save();
  ctx.translate(width * 0.56, height * 0.5);
  ctx.rotate(-0.1);
  ctx.scale(Math.min(width, height) / 760, Math.min(width, height) / 760);

  const drift = prefersReducedMotion ? 0 : Math.sin(time / 2400) * 5;
  ctx.beginPath();
  ctx.moveTo(-80, -245 + drift);
  ctx.bezierCurveTo(38, -232, 156, -164, 168, -48);
  ctx.bezierCurveTo(182, 86, 92, 178, 32, 232);
  ctx.bezierCurveTo(-35, 290, -142, 246, -165, 142);
  ctx.bezierCurveTo(-196, 12, -250, -56, -188, -142);
  ctx.bezierCurveTo(-156, -186, -132, -238, -80, -245 + drift);
  ctx.closePath();

  const gradient = ctx.createLinearGradient(-220, -250, 210, 260);
  gradient.addColorStop(0, "rgba(47, 107, 70, 0.62)");
  gradient.addColorStop(0.42, "rgba(45, 111, 137, 0.34)");
  gradient.addColorStop(0.72, "rgba(169, 85, 47, 0.34)");
  gradient.addColorStop(1, "rgba(196, 154, 68, 0.28)");
  ctx.fillStyle = gradient;
  ctx.fill();

  ctx.strokeStyle = "rgba(255, 253, 247, 0.22)";
  ctx.lineWidth = 1.2;
  ctx.stroke();
  ctx.restore();
}

function drawContours(time) {
  ctx.save();
  ctx.globalAlpha = 0.48;
  for (let index = 0; index < 9; index += 1) {
    const y = height * (0.15 + index * 0.1);
    const amplitude = 18 + index * 5;
    ctx.beginPath();
    for (let x = -40; x <= width + 40; x += 18) {
      const wave = Math.sin(x / 120 + index * 0.8 + time / 3800) * amplitude;
      const secondary = Math.cos(x / 70 + index + time / 5100) * 8;
      if (x === -40) {
        ctx.moveTo(x, y + wave + secondary);
      } else {
        ctx.lineTo(x, y + wave + secondary);
      }
    }
    ctx.strokeStyle = index % 3 === 0 ? "rgba(196, 154, 68, 0.22)" : "rgba(255, 253, 247, 0.12)";
    ctx.lineWidth = 1;
    ctx.stroke();
  }
  ctx.restore();
}

function drawNodes(time) {
  points.forEach((point, index) => {
    const motion = prefersReducedMotion ? 0 : Math.sin(time / 1600 + point.phase) * 6;
    point.x = point.baseX + Math.sin(time / 2100 + index) * 26;
    point.y = point.baseY + Math.cos(time / 2300 + point.phase) * 20 + motion;

    ctx.beginPath();
    ctx.fillStyle = point.color;
    ctx.globalAlpha = 0.76;
    ctx.arc(point.x, point.y, point.size, 0, Math.PI * 2);
    ctx.fill();
  });

  ctx.globalAlpha = 0.2;
  ctx.strokeStyle = "#fffdf7";
  for (let i = 0; i < points.length; i += 1) {
    const current = points[i];
    const next = points[(i + 7) % points.length];
    const distance = Math.hypot(current.x - next.x, current.y - next.y);
    if (distance < 240) {
      ctx.beginPath();
      ctx.moveTo(current.x, current.y);
      ctx.lineTo(next.x, next.y);
      ctx.stroke();
    }
  }
  ctx.globalAlpha = 1;
}

function draw(time) {
  ctx.clearRect(0, 0, width, height);
  ctx.fillStyle = "#14241e";
  ctx.fillRect(0, 0, width, height);
  drawContours(time);
  drawMapSilhouette(time);
  drawNodes(time);
}

function animate(time) {
  draw(time);
  if (!prefersReducedMotion) {
    animationFrame = requestAnimationFrame(animate);
  }
}

resize();
window.addEventListener("resize", resize);

if (prefersReducedMotion) {
  draw(0);
} else {
  animationFrame = requestAnimationFrame(animate);
}

window.addEventListener("beforeunload", () => {
  cancelAnimationFrame(animationFrame);
});

function openSupportModal(event) {
  lastSupportTrigger = event.currentTarget;
  if (typeof supportModal.showModal === "function") {
    supportModal.showModal();
    return;
  }
  supportModal.setAttribute("open", "");
}

function closeSupportModal() {
  if (typeof supportModal.close === "function") {
    supportModal.close();
  } else {
    supportModal.removeAttribute("open");
  }

  if (lastSupportTrigger) {
    lastSupportTrigger.focus();
  }
}

supportOpenButtons.forEach((button) => {
  button.addEventListener("click", openSupportModal);
});

supportCloseButtons.forEach((button) => {
  button.addEventListener("click", closeSupportModal);
});

supportModal.addEventListener("click", (event) => {
  if (event.target === supportModal) {
    closeSupportModal();
  }
});

supportModal.addEventListener("close", () => {
  if (lastSupportTrigger) {
    lastSupportTrigger.focus();
  }
});
