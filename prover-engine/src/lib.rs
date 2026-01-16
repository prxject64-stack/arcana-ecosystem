use pyo3::prelude::*;
use rayon::prelude::*;
use sha2::{Sha256, Digest};

#[pyfunction]
fn find_arcana_nonce(py: Python<'_>, target_prefix: String, range_start: u64, range_end: u64) -> PyResult<Option<u64>> {
    // DROP THE GIL: This allows all CPU cores to work at 100%
    py.allow_threads(|| {
        let result = (range_start..range_end)
            .into_par_iter() // The "Magic" that splits work across cores
            .find_map_any(|nonce| {
                let input = format!("{}{}", target_prefix, nonce);
                let mut hasher = Sha256::new();
                hasher.update(input.as_bytes());
                let hash = format!("{:x}", hasher.finalize());
                
                if hash.starts_with("00000") { // Simplified target logic
                    Some(nonce)
                } else {
                    None
                }
            });
        Ok(result)
    })
}

#[pymodule]
fn prover_engine(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(find_arcana_nonce, m)?)?;
    Ok(())
}
