
// devitations/cooldown_loop.js

/*
🧘 Devitation 04: Cooldown Loop
Reason: Meditation acts like a daily memory leak cleaner — preventing burnout.
*/

let energy = 100;

function cooldown(breaths = 5) {
  for (let i = 0; i < breaths; i++) {
    console.log("Inhale ⬆️");
    wait(3000);
    console.log("Hold 🫧");
    wait(2000);
    console.log("Exhale ⬇️");
    wait(4000);
    energy += 5;
  }
}

function wait(ms) {
  const start = Date.now();
  while (Date.now() < start + ms);
}

console.log("// System overheating… Initiating cooldown loop...");
cooldown();
console.log(`// Energy restored: ${energy}`);
